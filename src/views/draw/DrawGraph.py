import gc


class DrawGraph:
    def __init__(self):
        self.graph_size_y = 2
        self.graph_spread_y = 2
        self.graph_size_x = 1.25
        self.initial_y = 50
        self.initial_x = 20
        self.current_zero_line = self.initial_y
        self.tweet_count = 0
        self.rows = 0
        self.row_length = 1000
        self.started = False
        self.auto_updating = False

    def update_tweets(self):
        self.tweet_cursor = self.mongo_adapter.get_tweets()

    def update_graph(self, w, master, mongo_adapter):
        self.canvas = w
        self.master = master
        self.mongo_adapter = mongo_adapter
        self.current_zero_line = self.initial_y
        self.create_graph()

    def create_graph(self):
        self.update_tweets()
        self.tweet_list = list(self.tweet_cursor)
        self.tweet_count = 0
        self.rows = 0
        self.started = True
        last_point_x = self.tweet_count + self.initial_x
        last_point_y = self.initial_y

        self.create_infographic()

        for i in range(len(self.tweet_list)):

            self.tweet_count += 1

            if self.tweet_count > self.row_length:
                self.tweet_count = 0
                self.rows += 1
                last_point_x = self.tweet_count + self.initial_x
                last_point_y += self.initial_y
                self.current_zero_line += self.initial_y + self.graph_spread_y
                self.create_infographic()
                print('after ' + str(self.row_length))

            next_point_x = self.tweet_count * self.graph_size_x + self.initial_x
            next_point_y = self.current_zero_line + ((self.tweet_list[i]['mood'] * self.graph_size_y) / 3)

            self.canvas.create_line(last_point_x, last_point_y, next_point_x, next_point_y)

            last_point_x = next_point_x
            last_point_y = next_point_y

        # display total number of tweets, the row length and the last row length.
        if len(self.tweet_list) > 1000:
            self.canvas.create_text(1200, 18, text="<> = 1000 tweets")
        self.canvas.create_text(1200, 68 + self.graph_spread_y, text=str(len(self.tweet_list)) + ' total tweets to show')
        self.canvas.create_text(1200, 18 + (50 + self.graph_spread_y) * (len(self.tweet_list) // 1000), text='<> = ' + str(len(self.tweet_list) % 1000) + ' tweets')

        gc.collect()

        if self.auto_updating:
            self.update_tweets()
            self.master.after(1000, self.go_update)

    def create_infographic(self):
        # create lines to show information about the tweets
        # this happens every 1000 tweets for the next line, and one initially
        self.canvas.create_line(self.initial_x, self.current_zero_line, self.initial_x + 1100 * self.graph_size_x, self.current_zero_line, fill="blue", dash=(4, 4))
        self.canvas.create_line(self.initial_x, self.current_zero_line - 10 - self.graph_spread_y, self.initial_x + 1100 * self.graph_size_x, self.current_zero_line - 10 - self.graph_spread_y, fill="red", dash=(4, 4))
        self.canvas.create_line(self.initial_x, self.current_zero_line + 10 + self.graph_spread_y, self.initial_x + 1100 * self.graph_size_x, self.current_zero_line + 10 + self.graph_spread_y, fill="green", dash=(4, 4))

        # show information on the end of the lines
        self.canvas.create_text(self.initial_x + 1015 * self.graph_size_x, self.current_zero_line - 4 - self.graph_spread_y, text="-12")
        self.canvas.create_text(self.initial_x + 1015 * self.graph_size_x, self.current_zero_line + 4 + self.graph_spread_y, text="+12")

        # create colored backgrounds to make it easyer to read the graph
        self.canvas.create_rectangle(self.initial_x, self.current_zero_line, self.initial_x + 1000 * self.graph_size_x, self.current_zero_line - 10 - self.graph_spread_y, fill="red")
        self.canvas.create_rectangle(self.initial_x, self.current_zero_line, self.initial_x + 1000 * self.graph_size_x, self.current_zero_line + 10 + self.graph_spread_y, fill="green")

        # display the time to make the graph more useful
        try:
            # time = datetime from db, split on . (after . = miliseconds), take the first part (eg. 17:20:10)
            time = str(self.tweet_list[self.rows * self.row_length]["timestamp_ms"]).split('.')[0]
            self.canvas.create_text(80, self.current_zero_line - 17 - self.graph_spread_y, text=time)
        except:
            print('for some reason we cant print the first tweet of the row\'s time')

        try:
            # time = datetime from db like above, but now +500 tweets to show halfway the graph. There might not be
            # enough tweets so this except statement will get called a lot!
            time = str(self.tweet_list[self.rows * self.row_length + 500]["timestamp_ms"]).split('.')[0]
            self.canvas.create_text(580, self.current_zero_line - 17 - self.graph_spread_y, text=time)
        except:
            print('Not enough tweets to tell the time again')

    def increase_graph_size(self):
        self.graph_spread_y += 5
        self.graph_size_y += 1

    def decrease_graph_size(self):
        self.graph_spread_y -= 5
        self.graph_size_y -= 1

    def auto_update(self):
        if self.started:
            self.auto_updating = not self.auto_updating
            self.go_update()

    def go_update(self):
        self.canvas.delete("all")
        self.update_graph(self.canvas, self.master, self.mongo_adapter)
