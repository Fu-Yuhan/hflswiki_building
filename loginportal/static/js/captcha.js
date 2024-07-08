/*
 * @Author: Qinver
 * @Url: zibll.com
 * @Date: 2022-04-05 14:37:36
 * @LastEditTime: 2023-11-02 20:21:45
 */

function CaptchaInit() {
    var _mode = $('[machine-verification]');
    var mode = _mode.attr('machine-verification');
    var _body = $('body');
    window.captcha = {};

    function get_img(_this) {
        $.ajax({
            url: _win.uri + '/action/captcha.php',
            data: {
                type: 'image',
                id: _this.attr('imagecaptcha-id'),
            },
        }).done(function (data) {
            _this.html('<img alt="ç‚¹å‡»åˆ·æ–°" src="' + data.img + '">');
        });
    }

    switch (mode) {
        case 'image':
            var _code = $('.imagecaptcha');
            _code.each(function () {
                get_img($(this));
            });

            _body.on('click', '.imagecaptcha', function () {
                get_img($(this));
            });

            break;

        case 'slider':
            tbquire(['slidercaptcha']);

            break;
        case 'tcaptcha':
            var $btn = $('#TencentCaptcha.zib-tcaptcha');
            var appid = _mode.attr('tcaptcha-id');
            if (!$btn.length) {
                _body.append('<div class="hide zib-tcaptcha" id="TencentCaptcha" data-appid="' + appid + '" data-cbfn="TCaptchaOK" data-biz-state=""></div>');
            }
            tbquire(['tcaptcha-sdk']);

            break;

        case 'geetest':
            GeetestOpenInit(false);
            break;
    }
}
CaptchaInit();

/*global SliderCaptchaModal, initGeetest4*/
/**
 * æ‰“å¼€éªŒè¯ç å¼¹çª—
 * @param {object} _this - å½“å‰å¯¹è±¡
 * @param {string} mode - æ¨¡å¼ï¼Œå¯é€‰å€¼ä¸º'slider'ã€'geetest'ã€'tcaptcha'
 * @returns {number} - è¿”å›ž1è¡¨ç¤ºæ‰“å¼€å¤±è´¥
 */
function CaptchaOpen(_this, mode) {
    switch (mode) {
        case 'slider':
            tbquire(['slidercaptcha'], function () {
                SliderCaptchaModal('show', _this);
            });
            break;
        case 'geetest':
            window.captcha._this = _this;
            GeetestOpenInit(true);
            break;
        case 'tcaptcha':
            TCaptchaOpen(_this);
            break;
    }
    return !1;
}

//è…¾è®¯éªŒè¯ç å¼¹çª—
function TCaptchaOpen(_this) {
    window.captcha._this = _this;
    tbquire(['tcaptcha-sdk'], function () {
        $('#TencentCaptcha.zib-tcaptcha').click();
    });
}

function GeetestOpenInit(open) {
    var _mode = $('[machine-verification]');
    if (window.GeetestCaptcha) {
        open && window.GeetestCaptcha.showCaptcha();
        return;
    }
    if (!_mode.length) {
        return;
    }
    tbquire(['https://static.geetest.com/v4/gt4.js'], function () {
        initGeetest4(
            {
                captchaId: _mode.attr('geetest-id'),
                product: 'bind',
            },
            function (captchaObj) {
                captchaObj
                    .onReady(function () {
                        window.GeetestCaptcha = captchaObj;
                        open && captchaObj.showCaptcha();
                    })
                    .onSuccess(function () {
                        var getValidate = captchaObj.getValidate();
                        window.captcha.captcha_output = getValidate.captcha_output;
                        window.captcha.gen_time = getValidate.gen_time;
                        window.captcha.lot_number = getValidate.lot_number;
                        window.captcha.ticket = getValidate.pass_token;
                        window.captcha._this.click();
                    });
            }
        );
    });
}

//è…¾è®¯éªŒè¯ç å›žè°ƒ
function TCaptchaOK(res) {
    window.captcha.ticket = 0;
    window.captcha.randstr = 0;
    if (res.ret === 0) {
        window.captcha.ticket = res.ticket;
        window.captcha.randstr = res.randstr;
        window.captcha._this.click();
    }
}
