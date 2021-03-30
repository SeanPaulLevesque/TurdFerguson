from urllib.request import urlopen
import Classes as u
import json
import jsonpickle


#iterate through some episodes
for id in range(6821,6980,1):
    # grab webpage html
    url = "https://www.j-archive.com/showgame.php?game_id=" + str(id)
    page = urlopen(url)
    game_html = page.read().decode("utf-8")

    # init episode class
    curr_episode = u.ep()

    #populate jeopardy categories
    for attr, value in curr_episode.j.__dict__.items():
        #search text for category name tags
        start_index = game_html.find("<td class=\"category_name\">") + len("<td class=\"category_name\">")
        end_index = game_html.find("</td>", start_index)
        cat = game_html[start_index:end_index]
        game_html = game_html[end_index:]
        value.cat_name = cat

    #the HTML table is serialized left to right, then top to bottom
    #we want data shaped into categories so we can randomize the boards

    # populate first row jeopary questions
    for attr, value in curr_episode.j.__dict__.items():

        #check clue number to make sure we don't get misaligned with skipped questions
        question_index_start = game_html.find("toggle('clue_J_") + 15
        question_index_end = question_index_start + 1
        question_num = game_html[question_index_start:question_index_end]

        if (question_num == attr[8]):

            #answers are buried between these messes
            start_index = game_html.find("correct_response&quot;&gt;") + len("correct_response&quot;&gt;")
            end_index = game_html.find("&lt;/em&gt;&lt;br", start_index)
            value.clue1.answer = game_html[start_index:end_index]

            start_index = game_html.find("<td class=\"clue_value\">") + len("<td class=\"clue_value\">")
            end_index = game_html.find("</td>", start_index)
            value.clue1.value = game_html[start_index:end_index]

            start_index = game_html.find("class=\"clue_text\">") + len("class=\"clue_text\">")
            end_index = game_html.find("</td>", start_index)
            value.clue1.question = game_html[start_index:end_index]

            game_html = game_html[end_index:]

    # populate second row jeopary questions
    for attr, value in curr_episode.j.__dict__.items():

        question_index_start = game_html.find("toggle('clue_J_") + 15
        question_index_end = question_index_start + 1
        question_num = game_html[question_index_start:question_index_end]
        if (question_num == attr[8]):
            start_index = game_html.find("correct_response&quot;&gt;") + len("correct_response&quot;&gt;")
            end_index = game_html.find("&lt;/em&gt;&lt;br", start_index)
            value.clue2.answer = game_html[start_index:end_index]

            start_index = game_html.find("<td class=\"clue_value\">") + len("<td class=\"clue_value\">")
            end_index = game_html.find("</td>", start_index)
            value.clue2.value = game_html[start_index:end_index]

            start_index = game_html.find("class=\"clue_text\">") + len("class=\"clue_text\">")
            end_index = game_html.find("</td>", start_index)
            value.clue2.question = game_html[start_index:end_index]

            game_html = game_html[end_index:]

    # populate third row jeopary questions
    for attr, value in curr_episode.j.__dict__.items():
        # populate third row jeopary questions
        question_index_start = game_html.find("toggle('clue_J_") + 15
        question_index_end = question_index_start + 1
        question_num = game_html[question_index_start:question_index_end]
        if (question_num == attr[8]):
            start_index = game_html.find("correct_response&quot;&gt;") + len("correct_response&quot;&gt;")
            end_index = game_html.find("&lt;/em&gt;&lt;br", start_index)
            value.clue3.answer = game_html[start_index:end_index]

            start_index = game_html.find("<td class=\"clue_value\">") + len("<td class=\"clue_value\">")
            end_index = game_html.find("</td>", start_index)
            value.clue3.value = game_html[start_index:end_index]

            start_index = game_html.find("class=\"clue_text\">") + len("class=\"clue_text\">")
            end_index = game_html.find("</td>", start_index)
            value.clue3.question = game_html[start_index:end_index]

            game_html = game_html[end_index:]

    # populate fourth row jeopary questions
    for attr, value in curr_episode.j.__dict__.items():
        question_index_start = game_html.find("toggle('clue_J_") + 15
        question_index_end = question_index_start + 1
        question_num = game_html[question_index_start:question_index_end]
        if (question_num == attr[8]):
            start_index = game_html.find("correct_response&quot;&gt;") + len("correct_response&quot;&gt;")
            end_index = game_html.find("&lt;/em&gt;&lt;br", start_index)
            value.clue4.answer = game_html[start_index:end_index]

            start_index = game_html.find("<td class=\"clue_value\">") + len("<td class=\"clue_value\">")
            end_index = game_html.find("</td>", start_index)
            value.clue4.value = game_html[start_index:end_index]

            start_index = game_html.find("class=\"clue_text\">") + len("class=\"clue_text\">")
            end_index = game_html.find("</td>", start_index)
            value.clue4.question = game_html[start_index:end_index]

            game_html = game_html[end_index:]

    # populate fifth row jeopary questions
    for attr, value in curr_episode.j.__dict__.items():
        question_index_start = game_html.find("toggle('clue_J_") + 15
        question_index_end = question_index_start + 1
        question_num = game_html[question_index_start:question_index_end]
        if (question_num == attr[8]):
            start_index = game_html.find("correct_response&quot;&gt;") + len("correct_response&quot;&gt;")
            end_index = game_html.find("&lt;/em&gt;&lt;br", start_index)
            value.clue5.answer = game_html[start_index:end_index]

            start_index = game_html.find("<td class=\"clue_value\">") + len("<td class=\"clue_value\">")
            end_index = game_html.find("</td>", start_index)
            value.clue5.value = game_html[start_index:end_index]

            start_index = game_html.find("class=\"clue_text\">") + len("class=\"clue_text\">")
            end_index = game_html.find("</td>", start_index)
            value.clue5.question = game_html[start_index:end_index]

            game_html = game_html[end_index:]


    #populate double jeopardy categories
    for attr, value in curr_episode.d.__dict__.items():
        start_index = game_html.find("<td class=\"category_name\">") + len("<td class=\"category_name\">")
        end_index = game_html.find("</td>", start_index)
        cat = game_html[start_index:end_index]
        game_html = game_html[end_index:]
        value.cat_name = cat

    # populate first row double jeopary questions
    for attr, value in curr_episode.d.__dict__.items():
        question_index_start = game_html.find("toggle('clue_DJ_") + 16
        question_index_end = question_index_start + 1
        question_num = game_html[question_index_start:question_index_end]
        if (question_num == attr[8]):
            start_index = game_html.find("correct_response&quot;&gt;") + len("correct_response&quot;&gt;")
            end_index = game_html.find("&lt;/em&gt;&lt;br", start_index)
            value.clue1.answer = game_html[start_index:end_index]

            start_index = game_html.find("<td class=\"clue_value\">") + len("<td class=\"clue_value\">")
            end_index = game_html.find("</td>", start_index)
            value.clue1.value = game_html[start_index:end_index]

            start_index = game_html.find("class=\"clue_text\">") + len("class=\"clue_text\">")
            end_index = game_html.find("</td>", start_index)
            value.clue1.question = game_html[start_index:end_index]

            game_html = game_html[end_index:]

    # populate second row double jeopary questions
    for attr, value in curr_episode.d.__dict__.items():
        question_index_start = game_html.find("toggle('clue_DJ_") + 16
        question_index_end = question_index_start + 1
        question_num = game_html[question_index_start:question_index_end]
        if (question_num == attr[8]):
            start_index = game_html.find("correct_response&quot;&gt;") + len("correct_response&quot;&gt;")
            end_index = game_html.find("&lt;/em&gt;&lt;br", start_index)
            value.clue2.answer = game_html[start_index:end_index]

            start_index = game_html.find("<td class=\"clue_value\">") + len("<td class=\"clue_value\">")
            end_index = game_html.find("</td>", start_index)
            value.clue2.value = game_html[start_index:end_index]

            start_index = game_html.find("class=\"clue_text\">") + len("class=\"clue_text\">")
            end_index = game_html.find("</td>", start_index)
            value.clue2.question = game_html[start_index:end_index]

            game_html = game_html[end_index:]

    # populate third row double jeopary questions
    for attr, value in curr_episode.d.__dict__.items():
        question_index_start = game_html.find("toggle('clue_DJ_") + 16
        question_index_end = question_index_start + 1
        question_num = game_html[question_index_start:question_index_end]
        if (question_num == attr[8]):
            start_index = game_html.find("correct_response&quot;&gt;") + len("correct_response&quot;&gt;")
            end_index = game_html.find("&lt;/em&gt;&lt;br", start_index)
            value.clue3.answer = game_html[start_index:end_index]

            start_index = game_html.find("<td class=\"clue_value\">") + len("<td class=\"clue_value\">")
            end_index = game_html.find("</td>", start_index)
            value.clue3.value = game_html[start_index:end_index]

            start_index = game_html.find("class=\"clue_text\">") + len("class=\"clue_text\">")
            end_index = game_html.find("</td>", start_index)
            value.clue3.question = game_html[start_index:end_index]

            game_html = game_html[end_index:]

    # populate fourth row double jeopary questions
    for attr, value in curr_episode.d.__dict__.items():
        question_index_start = game_html.find("toggle('clue_DJ_") + 16
        question_index_end = question_index_start + 1
        question_num = game_html[question_index_start:question_index_end]
        if (question_num == attr[8]):
            start_index = game_html.find("correct_response&quot;&gt;") + len("correct_response&quot;&gt;")
            end_index = game_html.find("&lt;/em&gt;&lt;br", start_index)
            value.clue4.answer = game_html[start_index:end_index]

            start_index = game_html.find("<td class=\"clue_value\">") + len("<td class=\"clue_value\">")
            end_index = game_html.find("</td>", start_index)
            value.clue4.value = game_html[start_index:end_index]

            start_index = game_html.find("class=\"clue_text\">") + len("class=\"clue_text\">")
            end_index = game_html.find("</td>", start_index)
            value.clue4.question = game_html[start_index:end_index]

            game_html = game_html[end_index:]

    # populate fifth row double jeopary questions
    for attr, value in curr_episode.d.__dict__.items():
        question_index_start = game_html.find("toggle('clue_DJ_") + 16
        question_index_end = question_index_start + 1
        question_num = game_html[question_index_start:question_index_end]
        if (question_num == attr[8]):
            start_index = game_html.find("correct_response&quot;&gt;") + len("correct_response&quot;&gt;")
            end_index = game_html.find("&lt;/em&gt;&lt;br", start_index)
            value.clue5.answer = game_html[start_index:end_index]

            start_index = game_html.find("<td class=\"clue_value\">") + len("<td class=\"clue_value\">")
            end_index = game_html.find("</td>", start_index)
            value.clue5.value = game_html[start_index:end_index]

            start_index = game_html.find("class=\"clue_text\">") + len("class=\"clue_text\">")
            end_index = game_html.find("</td>", start_index)
            value.clue5.question = game_html[start_index:end_index]

            game_html = game_html[end_index:]

    # populate final jeopardy
    start_index = game_html.find("correct_response\&quot;&gt;") + len("correct_response\&quot;&gt;")
    end_index = game_html.find("&lt;/em&gt;')", start_index)
    curr_episode.f.answer = game_html[start_index:end_index]
    game_html = game_html[end_index:]

    start_index = game_html.find("<td class=\"category_name\">") + len("<td class=\"category_name\">")
    end_index = game_html.find("</td>", start_index)
    curr_episode.f.category = game_html[start_index:end_index]
    game_html = game_html[end_index:]

    start_index = game_html.find("<td id=\"clue_FJ\" class=\"clue_text\">") + len("<td id=\"clue_FJ\" class=\"clue_text\">")
    end_index = game_html.find("</td>", start_index)
    curr_episode.f.question = game_html[start_index:end_index]
    game_html = game_html[end_index:]

    json_object = jsonpickle.encode(curr_episode)

    with open('.\episodes\ID' + str(id) + '.txt', 'w+') as outfile:
        json.dump(json_object, outfile)
