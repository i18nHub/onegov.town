// intercooler has the abilty to redirect depending on response headers
// we'd like for it to do the same with our own 'redirect-after' attribute
$('a').on('success.ic', function(evt, elt, data, textStatus, xhr) {
    var redirect_after = $(elt).attr('redirect-after');
    if (! _.isUndefined(redirect_after)) {
        window.location = redirect_after;
    }

    return true;
});

// show the new content placeholder when hovering over the add content dropdown
$('.show-new-content-placeholder')
    .on('mouseenter', function() {
        var placeholder = $('<li>').
            text($(this).text())
            .addClass('new-content-placeholder');

        $('.children').append(placeholder);
        placeholder.show();
    })
    .on('mouseleave', function() {
        $('.new-content-placeholder').remove();
    });

// initialize all foundation functions
$(document).foundation();

// get the footer height and write it to the footer_height setting if possible
$(document).find('#footer_height').val($('footer > div').height() + 'px');

// Add image captions
$('.page-text img[alt][alt!=""]').each(function() {
    var caption = $("<span>").text($(this).attr('alt'));
    $(this).after(caption);
});

// Make sure files open in another window
$('.page-text a[href*="/datei/"]').attr('target', '_blank');
