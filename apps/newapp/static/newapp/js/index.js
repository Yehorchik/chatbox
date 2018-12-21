$(document).ready(function () {
    $("#info").click(function () {
        $(".your_info").toggle();
    });
});


$(document).ready(function () {
    $("#news").click(function () {
        $(".newon").toggle();
    });
});

$(document).ready(function () {
    $("#friends").click(function () {
        $(".myfriends").toggle();
    });
});

$(document).ready(function () {
    $("#your").click(function () {
        $(".mymessages").toggle();
    });
});

$(document).ready(function () {
    $("#send").click(function () {
        $(".send_message").toggle();
    });
});



$(document).on('click','.add',function(){
        console.log(this);
        var hello= this;
        var data = $(".add").serialize()   // capture all the data in the form in the variable data
        $.ajax({
            method: "POST",   // we are using a post request here, but this could also be done with a get
            url: this.action,
            data: data
        })
        .done(function(res){
            console.log(res);
            $('.allfriends').append(res);  // manipulate the dom when the response comes back
            $(hello).parent().hide();
        });
        return false

});

$(document).on('click', '.remove', function(){
        console.log(this);
        var remove= this;
        var data = $(".remove").serialize()   // capture all the data in the form in the variable data
        $.ajax({
            method: "POST",   // we are using a post request here, but this could also be done with a get
            url: this.action,
            data: data
        })
        .done(function(res){
            console.log(res);
            $('.findfriends').append(res);  // manipulate the dom when the response comes back
            $(remove).parent().hide();
        });
        return false

});

$(document).ready(function(){
    $('.shit').submit(function(){
       var done=this;
       var data = $(".shit").serialize()   // capture all the data in the form in the variable data
       $.ajax({
           method: "POST",   // we are using a post request here, but this could also be done with a get
           url: this.action,
           data: data
       }) 
        .done(function(res){   
             // manipulate the dom when the response comes back
            $(done).hide();
       });
        return false
    });


});


setTimeout(function() {
    $('.yes').fadeOut('fast');
}, 3000);

setTimeout(function() {
    $('.flash').fadeOut('fast');
}, 3000);