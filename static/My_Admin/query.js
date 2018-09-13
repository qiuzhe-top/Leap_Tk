function query_keyword() {
    a = $('#keyword').val()
    $('.get_msg').html('')
    $.ajax({
        url: '/myadmin/query_new',
        type: 'POST',
        data: {
            data: a
        },
        success: function (arg) {
            data = JSON.parse(arg.data);
            for (i in data) {
                text = "<tr>" + "<th>" + i + "</th>" + "<th>" + data[i].subject + "</th>" + "<th>" + data[i].id + "</th>" + "</tr>"
                $('.get_msg').append(text)
                console.log(data[i])
            }
        }

    })
}