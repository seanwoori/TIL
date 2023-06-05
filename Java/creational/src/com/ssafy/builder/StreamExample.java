package com.ssafy.builder;

import java.util.stream.Stream;

public class StreamExample {

    public static void main(String[] args) {
        Stream<String> names = Stream.<String>builder().add("stream").add("builder").build();
        names.forEach(System.out::println);
    }
}