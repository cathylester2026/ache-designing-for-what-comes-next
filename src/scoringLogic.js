export const RESILIENCE_DIMENSIONS = {
  'COMMIT NOW': 'foundation',
  'ENABLE FOR LATER': 'capacity',
  'EXPECT TO CHANGE': 'replaceability',
  "DON'T LOCK IN": 'optionality',
};

export function evaluateDesignPortfolio(items, explicitLockIn = false) {
  const dimensions = items.map(([, choice]) => RESILIENCE_DIMENSIONS[choice]);
  const coverage = [...new Set(dimensions.filter(Boolean))];
  const counts = dimensions.reduce((acc, dimension) => {
    acc[dimension] = (acc[dimension] || 0) + 1;
    return acc;
  }, {});

  const hasFoundation = coverage.includes('foundation');
  const hasAdaptiveLayer = coverage.some((d) =>
    ['capacity', 'replaceability', 'optionality'].includes(d)
  );

  let posture = 'STRAINS';
  let rationale = 'The portfolio protects some forms of resilience, but concentrates decisions in too few layers.';

  if (explicitLockIn) {
    posture = 'BREAKS';
    rationale = 'A current device, vendor, platform, or workflow was embedded as a hard building dependency.';
  } else if (coverage.length >= 3 || (hasFoundation && hasAdaptiveLayer && coverage.length >= 2 && items.length <= 2)) {
    posture = 'BENDS';
    rationale = 'The portfolio combines durable foundation with capacity, replaceability, or optionality.';
  }

  return {
    posture,
    rationale,
    coverage,
    counts,
    missing: ['foundation', 'capacity', 'replaceability', 'optionality'].filter(
      (dimension) => !coverage.includes(dimension)
    ),
  };
}
