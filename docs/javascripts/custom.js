const setupUiEnhancements = () => {
  document.querySelectorAll('.md-clipboard').forEach((button) => {
    if (button.dataset.toastBound === 'true') return;
    button.dataset.toastBound = 'true';

    button.addEventListener('click', () => {
      const toast = document.createElement('div');
      toast.textContent = 'Copied to clipboard!';
      toast.style.position = 'fixed';
      toast.style.bottom = '20px';
      toast.style.right = '20px';
      toast.style.background = 'var(--md-accent-fg-color)';
      toast.style.color = '#fff';
      toast.style.padding = '10px 20px';
      toast.style.borderRadius = '8px';
      toast.style.zIndex = '1000';
      document.body.appendChild(toast);
      setTimeout(() => toast.remove(), 1800);
    });
  });

  const searchInput = document.querySelector('.md-search__input');
  if (searchInput && searchInput.dataset.placeholderBound !== 'true') {
    searchInput.dataset.placeholderBound = 'true';
    const placeholders = ['Search documentation...', 'Find GPUs, SDKs...', 'Explore AI hardware...'];
    let index = 0;
    setInterval(() => {
      if (document.activeElement !== searchInput) {
        searchInput.placeholder = placeholders[index];
        index = (index + 1) % placeholders.length;
      }
    }, 3200);
  }

  document.querySelectorAll('.md-typeset h2, .md-typeset h3').forEach((heading) => {
    if (heading.id) {
      heading.style.scrollMarginTop = '4.5rem';
    }
  });
};

if (typeof window.document$ !== 'undefined') {
  window.document$.subscribe(setupUiEnhancements);
} else {
  document.addEventListener('DOMContentLoaded', setupUiEnhancements);
}