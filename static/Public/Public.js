function showtoastFromDiv() {
    $('.toast_div').toast({
        content: '这是默认的提示信息',
        duration: 1000
    });
}

function showtoastFromDivbottom() {
    $('.toast_div').toast({
        content: '这是默认的提示信息',
        duration: 3000,
        isCenter: false,
        animateIn: 'bounceIn-hastrans',
        animateOut: 'bounceOut-hastrans',
    });
}

function showtoastFromDocument(msg) {
    showMessage(msg);
}

function showtoastFromDocumentCenter(msg) {
    showMessage(msg, 3000, true, 'bounceInUp-hastrans', 'bounceOutDown-hastrans');
}

function toastbackground(msg) {
    $('body').toast({
        position: 'fixed',
        content: msg,
        duration: 3000,
        isCenter: false,
        background: '#00a0f0',
        animateIn: 'bounceIn-hastrans',
        animateOut: 'bounceOut-hastrans',
    });
}

function bounceInLeft(msg) {
    $('body').toast({
        position: 'fixed',
        content: msg,
        duration: 3000,
        isCenter: false,
        background: 'rgba(230,0,0,0.5)',
        animateIn: 'bounceInLeft-hastrans',
        animateOut: 'bounceOutRight-hastrans',
    });
}

function bounceInUp(msg) {
    $('body').toast({
        position: 'fixed',
        content: msg,
        duration: 3000,
        isCenter: false,
        background: '#4EA44E',
        animateIn: 'bounceInUp-hastrans',
        animateOut: 'bounceOutDown-hastrans',
    });
}