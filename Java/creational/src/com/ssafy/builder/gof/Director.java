package com.ssafy.builder.gof;

//각 문자열 포맷 빌드 과정을 템플릿화 시킨 디렉터
public class Director {
    private Builder builder;

    public Director(Builder builder) {
        this.builder = builder;
    }

    // 일종의 빌드 템플릿 메서드라 보면 된다
    public String build() {
        StringBuilder sb = new StringBuilder();

		// 빌더 구현체에서 정의한 생성 알고리즘이 실행됨
        sb.append(builder.head());
        sb.append(builder.body());
        sb.append(builder.foot());

        return sb.toString();
    }
}