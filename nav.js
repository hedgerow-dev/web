/* Shared nav — no inline handlers */
document.addEventListener('DOMContentLoaded', function () {
  var btn    = document.getElementById('navToggle');
  var drawer = document.getElementById('navDrawer');
  if (!btn || !drawer) return;

  function closeDrawer() {
    drawer.classList.remove('open');
    btn.classList.remove('open');
    btn.setAttribute('aria-expanded', 'false');
  }

  /* Hamburger toggle */
  btn.addEventListener('click', function () {
    var open = drawer.classList.toggle('open');
    btn.classList.toggle('open', open);
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  /* Close on link click */
  drawer.addEventListener('click', function (e) {
    if (e.target.tagName === 'A') closeDrawer();
  });

  /* Close on Escape key */
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeDrawer();
  });

  /* Auto-mark active page in drawer */
  var page = window.location.pathname.split('/').pop() || 'index.html';
  drawer.querySelectorAll('a[href]').forEach(function (a) {
    var href = a.getAttribute('href').split('#')[0].split('/').pop();
    if (href && href === page) {
      a.classList.add('active');
      a.style.color = 'var(--navy)';
      a.style.fontWeight = '600';
    }
  });
});
