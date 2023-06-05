package com.ssafy.builder;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.NoArgsConstructor;
import lombok.ToString;

@Builder
@ToString
public class LombokData {

    private String title;

    private int nights;

	private int days;
}
