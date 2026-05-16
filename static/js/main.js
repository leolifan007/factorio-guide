// Factorio Guide - Main JavaScript

(function() {
  'use strict';

  // Generate floating TOC from h2/h3 headings
  function buildTOC() {
    var toc = document.getElementById('floatingToc');
    if (!toc) return;

    var headings = document.querySelectorAll('.article-body h2, .article-body h3');
    if (headings.length === 0) {
      toc.style.display = 'none';
      return;
    }

    var tocList = document.createElement('ul');

    headings.forEach(function(heading) {
      var id = heading.id || heading.textContent.trim().toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
      heading.id = id;

      var li = document.createElement('li');
      var a = document.createElement('a');
      a.href = '#' + id;
      a.textContent = heading.textContent;

      if (heading.tagName === 'H3') {
        a.classList.add('toc-h3');
      }

      li.appendChild(a);
      tocList.appendChild(li);
    });

    toc.appendChild(tocList);
  }

  // Highlight active TOC item on scroll
  function highlightTOC() {
    var headings = document.querySelectorAll('.article-body h2, .article-body h3');
    if (headings.length === 0) return;

    var tocLinks = document.querySelectorAll('#floatingToc a');
    if (tocLinks.length === 0) return;

    var scrollY = window.scrollY;

    headings.forEach(function(heading, i) {
      var next = headings[i + 1];
      var top = heading.offsetTop - 100;
      var bottom = next ? next.offsetTop - 100 : document.body.scrollHeight;

      if (scrollY >= top && scrollY < bottom) {
        tocLinks.forEach(function(l) { l.classList.remove('active'); });
        var link = document.querySelector('#floatingToc a[href="#' + heading.id + '"]');
        if (link) link.classList.add('active');
      }
    });
  }

  // Scroll to heading on TOC click
  function tocClickHandler(e) {
    if (e.target.tagName === 'A') {
      e.preventDefault();
      var id = e.target.getAttribute('href').replace('#', '');
      var el = document.getElementById(id);
      if (el) {
        var top = el.offsetTop - 80;
        window.scrollTo({ top: top, behavior: 'smooth' });
      }
    }
  }

  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  function init() {
    buildTOC();
    highlightTOC();

    var toc = document.getElementById('floatingToc');
    if (toc) {
      toc.addEventListener('click', tocClickHandler);
    }

    window.addEventListener('scroll', highlightTOC, { passive: true });
  }
})();
