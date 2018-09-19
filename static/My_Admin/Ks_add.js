// 获取点击的课程然后返回小节
function For_section(obj){
        a = obj.value
        console.log(a)
        $.ajax({
        url:'/myadmin/For_section',
        type:'POST',
        data:{data:a},
        success:function(arg){
    }
})
}

