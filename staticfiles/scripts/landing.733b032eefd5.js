const $loginButton=$('#loginButton')
const $signupButton=$('#signupButton')
const $loginCard=$('#loginCard')
const $signupCard=$('#signupCard')
const $cancelButton=$('.cancelButton')

$loginCard.hide()
$signupCard.hide()
$loginButton.on("click",function(){
    $loginCard.show()
    $signupCard.hide()
})

$signupButton.on("click",function(){
    $signupCard.show()
    $loginCard.hide()
})

$cancelButton.on("click",function(){
    $signupCard.hide()
    $loginCard.hide()
})


