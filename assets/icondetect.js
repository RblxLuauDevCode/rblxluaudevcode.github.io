// please import jQuery and three.js first from codepen settings
// or this will doexist not working and will handle into error.

// iconDetect.js
function getFavicon() {
	var item = $("a.loadIcon");
	item.each(function () {
		var faviconUrl = $(this).attr("href");
		$(this).prepend(
			'<img src="https://www.google.com/s2/favicons?domain=' + faviconUrl + '">'
		);
	});
}

getFavicon();
