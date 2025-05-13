self.addEventListener("install", function (event) {
  event.waitUntil(
    caches.open("v1").then(function (cache) {
      return cache.addAll([
        "/",
        "/static/js/serviceworker.js",
        "/static/images/portfolio-icon.png",
        "/static/images/portfolio-icon2.png",
        "/static/manifest.json",
      ]);
    })
  );
});
