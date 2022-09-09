function getFavicon() {
    var item = $('a.link_has_favicon');
    item.each(function() {
        var faviconUrl = $(this).attr('href');
        $(this).prepend('<img src="http://www.google.com/s2/favicons?domain=' + faviconUrl + '">')
    });
}