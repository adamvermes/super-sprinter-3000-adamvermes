import csv

def save_story(form):
    all_stories = get_story()
    new_story = append_story(form)
    all_stories.append(new_story)
    write_to_file(all_stories)

    
def get_story():
    all_stories = []
    all_stories = [[story.strip() for story in stories.rstrip('\n').split(',')] for stories in open('form.csv')]
    return all_stories
        

def append_story(form):
    headers = ['Story Title', 'User Story', 'Acceptance Criteria', 'BV', 'Est', 'Status']
    append_story = []
    for header in headers:
        append_story.append(form[header])
    return append_story

def write_to_file(all_stories):
    with open('form.csv', 'w') as csv_file:
        for stories in all_stories:
            line = ",".join(stories)
            csv_file.write(line + "\n")
    