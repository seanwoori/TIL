package com.ssafy.builder.gof;

public class XMLBuilder extends Builder {
    public XMLBuilder(Data data) {
        super(data);
    }

    @Override
    public String head() {
        StringBuilder sb = new StringBuilder();

        sb.append("<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n");
        sb.append("<DATA>\n");

        return sb.toString();
    }

    @Override
    public String body() {
        StringBuilder sb = new StringBuilder();

        sb.append("\t<NAME>");
        sb.append(data.getName());
        sb.append("<NAME>");
        sb.append("\n\t<AGE>");
        sb.append(data.getAge());
        sb.append("<AGE>");

        return sb.toString();
    }

    @Override
    public String foot() {
        return "\n</DATA>";
    }
}