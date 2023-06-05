package com.ssafy.builder.gof;

 // Data 데이터들을 JSON 형태의 문자열로 변환해주는 빌더
public class JSONBuilder extends Builder {

    public JSONBuilder(Data data) {
        super(data);
    }

    @Override
    public String head() {
        return "{\n";
    }

    @Override
    public String body() {
        StringBuilder sb = new StringBuilder();

        sb.append("\t\"Name\" : ");
        sb.append("\"" + data.getName() + "\",\n");
        sb.append("\t\"Age\" : ");
        sb.append(data.getAge());

        return sb.toString();
    }

    @Override
    public String foot() {
        return "\n}";
    }
}