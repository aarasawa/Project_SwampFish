javascript:(function() {
  var encryptedFlag = ''; // encrypted flag would be here
  var key = "picoctf";
  var decryptedFlag = "";
  for (var i = 0; i < encryptedFlag.length; i++) {
      decryptedFlag += String.fromCharCode((encryptedFlag.charCodeAt(i) - key.charCodeAt(i % key.length) + 256) % 256);
  }
  alert(decryptedFlag);
})();
