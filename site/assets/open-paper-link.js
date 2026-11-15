const openApp = document.getElementById('open-app');
const paperIds = new URLSearchParams(window.location.search)
  .getAll(openApp.dataset.paperQuery);

if (paperIds.length) {
  const [paperId] = paperIds;
  if (paperIds.length === 1 && paperId.length && paperId.length <= 128 &&
      !/[^A-Za-z0-9_-]/.test(paperId)) {
    openApp.href = `${openApp.getAttribute('href')}/${paperId}`;
  } else {
    document.getElementById('link-notice').textContent =
      'This link has an invalid paper reference. Open ScoreIQ to browse the question paper library.';
  }
}
