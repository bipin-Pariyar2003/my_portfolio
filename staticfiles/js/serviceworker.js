self.addEventListener("install", function (event) {
  event.waitUntil(
    caches.open("v1").then(function (cache) {
      return cache.addAll([
        "/", // Only cache the root page
      ]);
    })
  );
});
