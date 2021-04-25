module.exports = {
    'Page header load test': function(browser) {
        browser
            .url('http://localhost:8080/')
            .waitForElementVisible('.brand')
            .assert.containsText(".brand", "Jester");

    },

    // 'My second test case': function(browser) {
    //     // entry point to nightwatch API 
    //     browser
    //         .url('http://localhost:8080/')
    //         .waitForElementVisible('.brand')
    //         .assert.containsText(".brand", "Jester");

    // }
}