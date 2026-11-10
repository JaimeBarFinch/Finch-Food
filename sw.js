/* Offline support. VERSION must change whenever any file changes (tools/build_data.py does it on every build),
   so phones fetch the new menu and offer to reload.
   The wine app lives on the same GitHub Pages address, so this worker only ever touches caches whose
   name starts with PREFIX, and it puts files back if another app has cleared them. */
var PREFIX = 'finch-food-';
var VERSION = 'finch-food-2026-11-10-b579a08c';
var FILES = [
  './', 'index.html', 'css/app.css', 'js/app.js', 'js/data.js', 'manifest.webmanifest',
  'fonts/Poppins-Light.ttf', 'fonts/Poppins-LightItalic.ttf', 'fonts/Poppins-Medium.ttf',
  'icons/icon-192.png', 'icons/icon-512.png', 'icons/icon-maskable-512.png', 'icons/apple-touch-icon.png'
];

self.addEventListener('install', function (e) {
  e.waitUntil(caches.open(VERSION).then(function (c) { return c.addAll(FILES); }));
});
self.addEventListener('activate', function (e) {
  e.waitUntil(caches.keys().then(function (keys) {
    return Promise.all(keys.filter(function (k) { return k.indexOf(PREFIX) === 0 && k !== VERSION; }).map(function (k) { return caches.delete(k); }));
  }).then(function () { return self.clients.claim(); }));
});
self.addEventListener('message', function (e) { if (e.data === 'skipWaiting') self.skipWaiting(); });
self.addEventListener('fetch', function (e) {
  if (e.request.method !== 'GET') return;
  e.respondWith(caches.open(VERSION).then(function (cache) {
    return cache.match(e.request, { ignoreSearch: true }).then(function (hit) {
      if (hit) return hit;
      return fetch(e.request).then(function (res) {
        if (res && res.ok && new URL(e.request.url).origin === location.origin) cache.put(e.request, res.clone());
        return res;
      }).catch(function () { return cache.match('index.html'); });
    });
  }));
});
