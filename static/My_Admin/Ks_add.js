// 获取点击的课程然后返回小节
var Section_number = new Object;
function For_section(obj){
        a = obj.value
        text2_data = ''
        text1_data = ''
        for(var key in Section_number){
            delete Section_number[key];
        }

        console.log('发送book ID:',a)
        $('#courseID').html('')
        $.ajax({
        url:'/myadmin/For_section',
        type:'POST',
        data:{data:a},
        beforeSend:function(){
            console.log('发送book ID:',a,'加载中......')
        },
        complete:function(){
            console.log('发送book ID:',a,'加载完成')
        },
        success:function(arg){
            for(i in arg.msg){
                data = JSON.parse(arg.msg[i]);
                console.log(data)
                for(j in data){
                    // console.log("单元》》",j)
                    text1_data = '<div class="input-group margin_top_10 unit_checkbox_box"><span class="input-group-addon"> ' + j + ' </span>'
                    for(k in data[j]){
                        // console.log("小节ID=",data[j][k].id)
                        // console.log("小节name=",data[j][k].title)
                        Section_number[data[j][k].id] = data[j][k].number
                        text2_data =  text2_data + '<label class="fancy-checkbox display-inline"><input name="check_unit" value="'+ data[j][k].id +'" type="checkbox"><span>' + data[j][k].title + '(' + data[j][k].number + ')' +'</span></label>'
                    }
                    $('#courseID').append(text1_data + text2_data + '</div>')
                    text1_data = ''
                    text2_data = ''
                }

            }
        }
})
} 
function Section_numbera(){
    console.log(Section_number)
}