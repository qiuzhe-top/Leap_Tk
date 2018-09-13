function Section_completion_ajax() {

    class_data = $('#class').val()
    minutia_data = $('#minutia').val()
    $.ajax({
        url: '/myadmin/Section_completion_ajax',
        type: 'POST',
        data: {
            class_data: class_data,
            minutia_data: minutia_data
        },
        beforeSend: function(){
            console.log("Londing")
        },
        success: function (arg) {
            data = JSON.parse(arg.msg);
            var num=0
            var name_data = new Array();
            var number_data = new Array();
            $('#usermsg_tbody').html("")
            // var name_data =""
            // var number_data =""
            for(i in data){
                num=num+1
                $('#usermsg_tbody').append("<tr>")
                $('#usermsg_tbody').append("<td>" + num + "</td>")
                $('#usermsg_tbody').append("<td>" + data[i][0] + "</td>")
                $('#usermsg_tbody').append("<td>" + data[i][1] + "</td>")
                $('#usermsg_tbody').append("<td>" + data[i][2] + "</td>")
                $('#usermsg_tbody').append("<td>" + data[i][3] + "</td>")
                $('#usermsg_tbody').append("<td>" + data[i][4] + "</td>")
                $('#usermsg_tbody').append("</tr>")
                name_data.push(data[i][0])
                number_data.push(data[i][1])
            }
            console.log(name_data,number_data)
            charts(name_data,number_data)
        }
    })

    
    
    
}
function charts(name_data,number_data){
    var options;
    // name_data = ['J11an', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    // number_data = [200, 380, 350, 320, 410, 450, 570, 400, 555, 620, 750, 900]
    var data = {
        labels: name_data,
        series: [
            number_data,
        ]
    };
    // line chart
    options = {
        height: "500px",
        showPoint: true,
        axisX: {
            showGrid: false
        },
        lineSmooth: false,
    };
    new Chartist.Line('#demo-line-chart', data, options);
}