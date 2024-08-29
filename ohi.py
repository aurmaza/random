  private String formatDateTime(JsonNode dateTimeNode) {
        String year = dateTimeNode.path("date").path("year").asText();
        String month = String.format("%02d", dateTimeNode.path("date").path("month").asInt());
        String day = String.format("%02d", dateTimeNode.path("date").path("day").asInt());
        String hour = String.format("%02d", dateTimeNode.path("time").path("hour").asInt());
        String minute = String.format("%02d", dateTimeNode.path("time").path("minute").asInt());
        String second = String.format("%02d", dateTimeNode.path("time").path("second").asInt());

        return year + "-" + month + "-" + day + " " + hour + ":" + minute + ":" + second;
    }
