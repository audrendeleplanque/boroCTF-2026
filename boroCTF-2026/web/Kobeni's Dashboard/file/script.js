(function () {
	// Create an iframe, inject a small script into its head that loads
	// the Cloudflare challenge script from /cdn-cgi/... when the iframe
	// document is available.

	function injectIntoIframe() {
		var iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
		if (!iframeDoc) return;

		// Build a script element containing the CF params and dynamic loader
		var inlineScript = iframeDoc.createElement('script');
		inlineScript.innerHTML = "window.__CF$cv$params={r:'a0b215175dced5c9',t:'MTc4MTM2NDA1OA=='};" +
			"var s=document.createElement('script');s.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js';document.getElementsByTagName('head')[0].appendChild(s);";

		// Append the inline script into the iframe head
		var head = iframeDoc.getElementsByTagName('head')[0];
		if (head) head.appendChild(inlineScript);
	}

	if (document.body) {
		var iframe = document.createElement('iframe');
		iframe.height = 1;
		iframe.width = 1;
		iframe.style.position = 'absolute';
		iframe.style.top = '0';
		iframe.style.left = '0';
		iframe.style.border = 'none';
		iframe.style.visibility = 'hidden';

		document.body.appendChild(iframe);

		if (document.readyState !== 'loading') {
			injectIntoIframe();
		} else if (window.addEventListener) {
			document.addEventListener('DOMContentLoaded', injectIntoIframe);
		} else {
			// Older IE fallback
			var previousReady = document.onreadystatechange || function () {};
			document.onreadystatechange = function (ev) {
				previousReady(ev);
				if (document.readyState !== 'loading') {
					document.onreadystatechange = previousReady;
					injectIntoIframe();
				}
			};
		}
	}
})();