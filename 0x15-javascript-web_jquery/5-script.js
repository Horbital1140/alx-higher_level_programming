$(document).ready(function () {
    $('DIV#add_item').click(function () {
        var newlist = $('<li>Item</li>');
        ('UL.my_list').append(newlist);
    });
});
