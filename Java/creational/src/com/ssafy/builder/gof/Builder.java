package com.ssafy.builder.gof;

public abstract class Builder {
    // 상속한 자식 클래스에서 사용하도록 protected 접근제어자 지정
    protected Data data;

    public Builder(Data data) {
        this.data = data;
    }

    // Data 객체의 데이터들을 원하는 형태의 문자열 포맷을 해주는 메서드들 (머리 - 중간 - 끝 형식)
    public abstract String head();
    public abstract String body();
    public abstract String foot();

}