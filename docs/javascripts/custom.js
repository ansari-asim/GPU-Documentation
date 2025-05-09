document.addEventListener('DOMContentLoaded', () => {
    // Toast notification for code copy
    document.querySelectorAll('.md-clipboard').forEach(button => {
      button.addEventListener('click', () => {
        const toast = document.createElement('div');
        toast.textContent = 'Copied to clipboard!';
        toast.style.position = 'fixed';
        toast.style.bottom = '20px';
        toast.style.right = '20px';
        toast.style.background = 'var(--md-accent-fg-color)';
        toast.style.color = '#fff';
        toast.style.padding = '10px 20px';
        toast.style.borderRadius = '5px';
        toast.style.zIndex = '1000';
        document.body.appendChild(toast);
        setTimeout(() => toast.remove(), 2000);
      });
    });

    // Search bar placeholder animation
    const searchInput = document.querySelector('.md-search__input');
    if (searchInput) {
      const placeholders = ['Search documentation...', 'Find GPUs, SDKs...', 'Explore AI hardware...'];
      let index = 0;
      setInterval(() => {
        searchInput.placeholder = placeholders[index];
        index = (index + 1) % placeholders.length;
      }, 3000);
    }
  });