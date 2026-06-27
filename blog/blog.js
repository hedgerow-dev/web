// blog.js: topic filtering for the post list
(function () {
  var filterBar = document.getElementById('tagFilter');
  if (!filterBar) return;

  var buttons = Array.prototype.slice.call(filterBar.querySelectorAll('.tag-filter-btn'));
  var cards = Array.prototype.slice.call(document.querySelectorAll('.post-card'));
  var empty = document.getElementById('postListEmpty');

  function apply(filter) {
    var visible = 0;
    cards.forEach(function (card) {
      var tags = (card.getAttribute('data-tags') || '').split(/\s+/);
      var show = filter === 'all' || tags.indexOf(filter) !== -1;
      card.classList.toggle('is-hidden', !show);
      if (show) visible++;
    });
    if (empty) empty.classList.toggle('show', visible === 0);
  }

  filterBar.addEventListener('click', function (e) {
    var btn = e.target.closest('.tag-filter-btn');
    if (!btn) return;
    buttons.forEach(function (b) { b.classList.remove('active'); });
    btn.classList.add('active');
    apply(btn.getAttribute('data-filter'));
  });
})();
