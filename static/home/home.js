

window.onload = function () {
    if ("ActiveXObject" in window) {
        if (confirm("检测到你是IE浏览器，部分功能无法使用，是否下载Chrome浏览器")){ 
            window.location.href="/static/Other/chrome.exe" 
            }
    } else {
   
    }
    document.getElementById('books_data').value = index
}
$(function () {
    $(".matter_li").click(function () {
        $(this).addClass("active_list").siblings().removeClass("active_list");
        $('.ma_list').addClass("active_list").siblings().removeClass("active_list");
        $(".ma_list").eq($(this).index()).addClass("active_list_box").siblings().removeClass("active_list_box");
    })


})

function books_up(obj) {
    $.ajax({
        url: 'updata_user_book',
        type: 'POST',
        data: {
            data: obj.value
        },
        complete: function () {
            window.location.reload()
        },
        success: function (arg) {
            // alert(arg.msg)
        }
    })
}

function rank_updata() {

    $.ajax({
        url: 'rank_updata',
        type: 'POST',
        data: {
            data: ""
        },
        beforeSend: function () {
            $("#rank_data_text").text('排名中...')
        },
        complete: function () {
            $("#rank_data_text").text('排名')

        },
        success: function (arg) {
            document.getElementById('rank_data').innerHTML = arg.msg
        }
    })
}

// 修改密码
function new_password_ajax() {
    a = $('.pawsword_old').val()
    b = $('.pawsword_new1').val()
    c = $('.pawsword_new2').val()
    if (b == c) {
        var new_pawsword = b
        var pawsword = a

        $.ajax({
            url: 'user_password_ajax',
            type: 'POST',
            data: {
                new_password: new_pawsword,
                password: pawsword
            },
            beforeSend: function () {
                console.log("加载中。。。")
                $("#new_password_but").attr("disabled", 'disabled');
                $("#new_password_but").text('修改中...')
            },
            complete: function () {
                console.log("加载完成。。。")
                $("#new_password_but").removeAttr("disabled");

            },
            success: function (arg) {
                console.log("返回数据")
                console.log(arg.msg)
                $("#new_password_but").text(arg.msg)
            }
        })

    }
}


// function user_Collection(){
//     $.ajax({
//         url:'user_Collection_ajax',
//         type:'POST',
//         data:{data:""},
//         success:function(arg){
//             document.getElementById('rank_data').innerHTML=arg.msg
//         }
//     })
// }

// function user_Error(){
//     $.ajax({
//         url:'user_Error_ajax',
//         type:'POST',
//         data:{data:""},
//         success:function(arg){
//             document.getElementById('rank_data').innerHTML=arg.msg
//         }
//     })
// }

function Delete_the_title(obj) {
    // var va = "'" + 'va' + obj.value  + "'"
    // var va = 'va' + obj.value 
    // console.log(va)
    // $(va).addClass('isplay-none')
    // a = document.getElementsByClassName(va)[0]//.addClass('display-none')
    // document.getElementsByClassName(va)[0].removeChild()//.addClass('display-none')
    // console.log(a)
    $.ajax({
        url: '/Answer/Delete_the_title',
        type: 'POST',
        data: {
            data: obj.value
        },
        complete: function () {},
        success: function (arg) {
            // document.getElementById('rank_data').innerHTML=arg.msg
        }
    })
}