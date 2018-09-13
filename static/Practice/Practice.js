var but = true

$(document).ready(function () {
    $("#flip").click(function () {
        $("#panel").slideToggle("200");
    });
});
$(function () {
    // 答题卡点击事件
    $(".nav_content li").click(function () {
        $(this).addClass("boder").siblings().removeClass("boder");
        obj_id = $(".boder").val()
        console.log(obj_id)
        boj_ajax(obj_id)
    });
    // 收藏按钮
    $(".ico_empty").click(function () {
        a = $('.boder').val()
        if (but) {
            but = false
        } else {
            but = true
        }
        obj_id = $(".boder").val()
        if (but) {
            $('.ico_empty').addClass("glyphicon-star").removeClass("glyphicon-star-empty");
            ty = 1
            Collection(obj_id, ty)
        } else {
            $('.ico_empty').addClass("glyphicon-star-empty").removeClass("glyphicon-star");
            ty = 2
            Collection(obj_id, ty)
        }
        console.log(a)
    });

    // 答题卡展开按钮
    var but2 = true
    $(".ico_large").click(function () {
        if (but2) {
            $(this).addClass("ico_large_act");
            but2 = false
        } else {
            $(this).removeClass("ico_large_act");
            but2 = true
        }
    });
    // 点击选项生成答案 > ajax判断对错
    $(".subject_options input").click(function () {
        // 获取答案
        obj = document.getElementsByName('gender')
        answer = ''
        for (k in obj) {
            if (obj[k].type == "radio") {
                if (obj[k].checked) {
                    answer = obj[k].value
                }
            }
        }

        obj_id = $(".boder").val()
        if (answer != '') {
            IF_subject_ajax(obj_id, answer)
            console.log(answer)
        }
    });
});
// 改变属性为checkbox
// for(i=0;i<obj.length;i++){
//     obj[i].type='checkbox'
//     obj[i].checked=false
// }
// $('.answerA').removeClass("display-none")
// $('.answerB').removeClass("display-none")
// $('.answerC').removeClass("display-none")
// $('.answerD').removeClass("display-none")
// $('.answerE').removeClass("display-none")
// $('.answerF').removeClass("display-none")
// $('.fancy-radio').addClass("fancy-checkbox").removeClass("fancy-radio")

// 改变属性为radio
// for(i=0;i<obj.length;i++){
//     obj[i].type='radio'
//     obj[i].checked=false
// }
// $('.answerA').removeClass("display-none")
// $('.answerB').removeClass("display-none")
// $('.answerC').removeClass("display-none")
// $('.answerD').removeClass("display-none")
// $('.answerE').addClass("display-none")
// $('.answerF').addClass("display-none")
// $('.fancy-checkbox').addClass("fancy-radio").removeClass("fancy-checkbox")

// 上一题
function prev_sub() {
    obj_id = $(".boder").prev().val()
    $(".boder").prev().addClass("boder").siblings().removeClass("boder");
    boj_ajax(obj_id)
    if ($(".boder").index() == 0) {
        $(".prev_sub").addClass('display-none')
    }
    $(".next_sub").removeClass('display-none')
}
// 下一题
function next_sub() {
    obj_id = $(".boder").next().val()
    $(".boder").next().addClass("boder").siblings().removeClass("boder");
    // console.log(obj_id)
    boj_ajax(obj_id)
    var boder_index = $(".boder").index()
    $(".prev_sub").removeClass('display-none')
    if (boder_index == $('.milix').length - 1) {
        $(".next_sub").addClass('display-none')
    }
}

// 根据题目id获取题目信息
function boj_ajax(obj_id) {
    obj = document.getElementsByName('gender')
    i = '<i></i>'
    $('.ico_sign').addClass('display-none')
    $('.boj_if_ico').addClass('display-none')
    if (obj_id != undefined) {
        $.ajax({
            url: '/Answer/boj_ajax',
            type: 'POST',
            data: {
                id: obj_id
            },
            beforeSend: function () {
                $(".next_sub").attr("disabled", 'disabled');
                $(".prev_sub").attr("disabled", 'disabled');
            },
            complete: function () {
                $(".next_sub").removeAttr("disabled");
                $(".prev_sub").removeAttr("disabled");
            },
            success: function (arg) {
                $('.obj_title').html(arg.list[0])

                if (arg.list[1] == "单选") {
                    for (j = 0; j < obj.length; j++) {
                        obj[j].type = 'radio'
                        obj[j].checked = false
                    }
                    $('.fancy-checkbox').addClass("fancy-radio").removeClass("fancy-checkbox")
                    $('.answerA span').html(i + arg.list[2])
                    $('.answerB span').html(i + arg.list[3])
                    $('.answerC span').html(i + arg.list[4])
                    $('.answerD span').html(i + arg.list[5])

                    $('.fancy-radio').removeClass("display-none")
                    $('.answerE').addClass('display-none')
                    $('.answerF').addClass('display-none')
                    $('.answerno').addClass('display-none')
                    $('.answeryes').addClass('display-none')
                } else if (arg.list[1] == "多选") {
                    for (j = 0; j < obj.length; j++) {
                        obj[j].type = 'checkbox'
                        obj[j].checked = false
                    }
                    $('.fancy-radio').addClass("fancy-checkbox").removeClass("fancy-radio")
                    $('.fancy-checkbox').removeClass("display-none")
                    $('.answerno').addClass('display-none')
                    $('.answeryes').addClass('display-none')
                    $('.answerA span').html(i + arg.list[2])
                    $('.answerB span').html(i + arg.list[3])
                    $('.answerC span').html(i + arg.list[4])
                    $('.answerD span').html(i + arg.list[5])
                    $('.answerE span').html(i + arg.list[6])
                    $('.answerF span').html(i + arg.list[7])

                    $('.ico_sign').removeClass('display-none')
                    // console.log(obj_id,'触发removeClass')

                } else {
                    for (j = 0; j < obj.length; j++) {
                        obj[j].type = 'radio'
                        obj[j].checked = false
                    }
                    $('.fancy-checkbox').addClass("fancy-radio").removeClass("fancy-checkbox")
                    $('.fancy-radio').addClass("display-none")
                    $('.answerno').removeClass('display-none')
                    $('.answeryes').removeClass('display-none')
                    $('.answerno span').html(i + "错误")
                    $('.answeryes span').html(i + "正确")
                }
                if (arg.tm_Collection == "glyphicon-star-empty") {
                    but = false
                } else {
                    but = true
                }

                $('.ico_empty').removeClass('glyphicon-star-empty').removeClass('glyphicon-star').addClass(arg.tm_Collection)
            }
        })
    }
}
// 收藏题目
function Collection(obj_id, ty) {
    $.ajax({
        url: '/Answer/Collection_ajax',
        type: 'POST',
        data: {
            id: obj_id,
            ty: ty
        },
        success: function (arg) {

        }
    })
}

function show_checked_aws() {
    // 获取答案
    obj = document.getElementsByName('gender')
    answer = ''
    for (k in obj) {
        if (obj[k].type == "checkbox") {
            if (obj[k].checked) {
                answer = answer + obj[k].value
            }
        }
    }
    if (answer != '') {
        obj_id = $(".boder").val()
        IF_subject_ajax(obj_id, answer)
        console.log(answer)
    }
}

function IF_subject_ajax(obj_id, answer) {
    if (typeof (obj_id) != 'undefined') {
        console.log(obj_id, answer)
        $.ajax({
            url: '/Answer/IF_subject_ajax',
            type: 'POST',
            data: {
                id: obj_id,
                answer: answer
            },
            success: function (arg) {
                aw = arg.msg
                console.log(arg.msg)
                if (aw == "yes") {
                    $('.boj_if_ico').addClass('glyphicon-ok')
                    $('.boj_if_ico').removeClass('glyphicon-remove')
                    $('.boj_if_ico').removeClass('display-none')
                } else if (aw == "no") {
                    $('.boj_if_ico').removeClass('display-none')
                    $('.boj_if_ico').removeClass('glyphicon-ok')
                    $('.boj_if_ico').addClass('glyphicon-remove')
                }
            }
        })
    }
}