package com.ssafy.behavioral.templatemethod;

public class ImplementationB extends AbstractTemplate {

    @Override
    protected void step1() {}

    @Override
    protected void step2() {}

    @Override
    protected void step3() {}

    // hook 메소드를 오버라이드 해서 false로 하여 템플릿에서 마지막 로직이 실행되지 않도록 설정
    @Override
    protected boolean hook() {
        return false;
    }
}