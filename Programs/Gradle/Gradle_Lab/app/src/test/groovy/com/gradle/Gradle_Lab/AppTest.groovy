package com.gradle.Gradle_Lab

import spock.lang.Specification


class AppTest extends Specification {

    def "Today's Test"(){
        setup:
        def x = 12
        def y = 21
        def z

        when:
        z = x+y

        then:
        z == 33

    }

}