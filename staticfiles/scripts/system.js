
const $editButton=$('#systemEditButton')
const $editPop=$('#editPop')
const $cancelButton=$('.cancelButton')

$editPop.hide()
$editButton.on("click",function(){
    $editPop.show()
})

$cancelButton.on("click",function(){
    $editPop.hide()
})