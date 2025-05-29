window.onload = function () {
  const viewer = document.querySelector('spline-viewer');

  const interval = setInterval(() => {
    const shadow = viewer.shadowRoot;
    const logo = shadow && shadow.querySelector('#logo');
    if (logo) {
      logo.remove();
      clearInterval(interval);
    }
  }, 100);
};
