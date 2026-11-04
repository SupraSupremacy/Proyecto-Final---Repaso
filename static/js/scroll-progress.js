const progress = document.getElementById('scrollProgress');

function updateScrollProgress() {
    if (!progress) {
        return;
    }
    const scrollTop = window.scrollY || document.documentElement.scrollTop || 0;
    const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
    const ratio = scrollHeight > 0 ? (scrollTop / scrollHeight) * 100 : 0;
    progress.style.width = Math.min(100, Math.max(0, ratio)) + '%';
}

if (progress) {
    updateScrollProgress();
    window.addEventListener('scroll', updateScrollProgress, { passive: true });
    window.addEventListener('resize', updateScrollProgress);
}
