
/*
    Test if take photo, start video, and stop video buttons work as expected.
    A device camera is required for these tests to pass. 
*/

module.exports = {
    
    // Test if take photo button adds photo to the gallery
    'Take photo button test': function(browser) {
        browser
            .url('http://localhost:8080/')
            .waitForElementVisible('#photo')
            .click("#photo", function(){       // Click take photo button
                browser
                    .click("#galleryButton", function(){    // Then move to gallery tab
                        browser
                            .waitForElementVisible('#image')
                            .assert.elementPresent('#image');                 
                    })          
            })
    },

    // 'Take video button test': function(browser) {
    //     browser
    //         .url('http://localhost:8080/')
    //         .waitForElementVisible('#record')
    //         .click('#record', setTimeout(function(){    // Click start recording button, 
    //             browser
    //                 .click('#stop', function() {        // Click stop recording after 1 second
    //                     browser
    //                         .click("#galleryButton", function(){    // Move to gallery tab
    //                             browser
    //                                 .waitForElementVisible('#recorded') // Check if video is there
    //                                 .assert.elementPresent('#recorded');                 
    //                         })
    //                 }
    //                 )       
    //         }, 2000));
    // }
 
   
    // make sure "no photos" is no longer displaying 

    //test download?
}