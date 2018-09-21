// 获取点击的课程然后返回小节
function For_section(obj){
        a = obj.value
        console.log(a)
        $.ajax({
        url:'/myadmin/For_section',
        type:'POST',
        data:{data:a},
        success:function(arg){
            // console.log(arg['0'])
            // data = JSON.parse(arg);
            // console.log(data)
            for(i in arg.msg){
                da = arg.msg[i]
                da =  JSON.parse(da)
                for(i in da){
                    console.log(i)
                    da1 = JSON.parse(da[i])
                    console.log(da1)
                    
                    // for(i in da1){
                    //     console.log(da1[i])
                        
                    // }
                }
            }
    }
})
} 

