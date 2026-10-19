# Designing for What Comes Next

Interactive ACHE healthcare design decision simulation built with React and Vite.

## Upload to GitHub

1. Create a new GitHub repository and leave it empty.
2. Unzip this package on your computer.
3. In the repository, choose **Add file** > **Upload files**.
4. Drag every unzipped item into the upload area, including the `.github`, `public`, and `src` folders.
5. Commit the files to the `main` branch.
6. Open **Settings** > **Pages**.
7. Under **Build and deployment**, set **Source** to **GitHub Actions**.
8. Open the **Actions** tab. The workflow named **Deploy to GitHub Pages** will build and publish the app.
9. When the workflow shows a green check, return to **Settings** > **Pages** to open the published site.

## Local test (optional)

```bash
npm install
npm run dev
```

## Important

All images are local in `public/images`. The app contains no `sandbox://` image links and uses `base: './'` for GitHub Pages compatibility.
