package com.ssafy.structural.chainofresponsibility;

//구체적인 핸들러를 묶는 인터페이스 (추상 클래스)
public abstract class Handler {
    // 다음 체인으로 연결될 핸들러
    protected Handler nextHandler = null;

    // 생성자를 통해 연결시킬 핸들러를 등록
    public Handler setNext(Handler handler) {
        this.nextHandler = handler;
        return handler; // 메서드 체이닝 구성을 위해 인자를 그대로 반환함
    }

    // 자식 핸들러에서 구체화 하는 추상 메서드
    protected abstract void process(String url);

    // 핸들러가 요청에 대해 처리하는 메서드 
    public void run(String url) {
        process(url);

        // 만일 핸들러가 연결된게 있다면 다음 핸들러로 책임을 떠넘긴다
        if (nextHandler != null)
            nextHandler.run(url);
    }
}