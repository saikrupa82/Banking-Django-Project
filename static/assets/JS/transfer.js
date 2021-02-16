$('#the-modal').on('show', function() {
    $('body').append('<div class="modal-backdrop"></div>');
});
$('#the-modal').on('hide', function() {
    $('body').find('.modal-backdrop').remove();
});
$('#the-modal').modal();