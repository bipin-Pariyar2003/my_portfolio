self.addEventListener("install", function (e) {
  e.waitUntil(
    caches.open("portfolio-cache").then(function (cache) {
      return cache.addAll(["/", "/static/css/styles.css", "/static/js/main.js"]);
    })
  );
});

self.addEventListener("fetch", function (e) {
  e.respondWith(
    caches.match(e.request).then(function (response) {
      return response || fetch(e.request);
    })
  );
});
