$(document).ready(function() {
    $('#rainbowCycleBtn').on('click', function(e){
        $.ajax({
            url: '/piapp?status=rc',
            method: 'GET',
            success: function(result) {
                console.log(result);
         }
        });
        e.preventDefault();
    });
    
    $('#turnOffBtn').on('click', function(e){
        $.ajax({
            url: '/piapp?status=off',
            method: 'GET',
            success: function(result) {
                console.log(result);
         }
        });
        e.preventDefault();
    });
});
