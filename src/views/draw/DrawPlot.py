import gc


class DrawPlot:
    def __init__(self, mongo_adapter):
        self.plot_distance = 6
        self.plot_ora_item_size = 5
        self.plot_red_item_size = 1
        self.plot_devider = 10
        self.red_spacer = 2
        self.initial_x = 0
        self.current_zero_line = 350
        self.graph_spread_y = 3
        self.started = False
        self.auto_updating = False
        self.mongo_adapter = mongo_adapter

    def update_tweets(self):
        self.tweet_cursor = self.mongo_adapter.get_tweets()

    def update_plot(self, w, master):
        self.update_tweets()
        self.started = True
        self.master = master
        self.canvas = w

        tweet_list = list(self.tweet_cursor)

        tweet_count = 0

        # draw items for the plot
        for tweet in tweet_list:
            plot_start_x = tweet_count / self.plot_devider + self.initial_x
            plot_start_y = tweet['mood'] * self.plot_distance + self.current_zero_line - (self.plot_ora_item_size / 2)
            plot_end_x = plot_start_x + self.plot_ora_item_size
            plot_end_y = plot_start_y + self.plot_ora_item_size

            tweet_count += 1

            w.create_rectangle(plot_start_x, plot_start_y, plot_end_x, plot_end_y, fill='orange', outline='orange')

        tweet_count = 0

        for tweet in tweet_list:
            plot_start_x = tweet_count / self.plot_devider + self.initial_x + self.red_spacer
            plot_start_y = tweet['mood'] * self.plot_distance + self.current_zero_line - self.plot_red_item_size
            plot_end_x = plot_start_x + self.plot_red_item_size
            plot_end_y = plot_start_y + self.plot_red_item_size

            tweet_count += 1
            w.create_rectangle(plot_start_x, plot_start_y, plot_end_x, plot_end_y, fill='red', outline='red')

            if tweet_count % 1000 == 0 and tweet_count <= 12000:
                date_time = str(tweet['timestamp_ms']).split('.')[0]
                date = date_time.split(' ')[0]
                time = date_time.split(' ')[1]

                w.create_text(plot_start_x, 50, text=date)
                w.create_text(plot_start_x, 80, text=time)
                w.create_line(plot_start_x, 100, plot_start_x, 900, dash=(4, 2), fill='gray')

        self.create_infographic()
        gc.collect()

        if self.auto_updating:
            self.update_tweets()
            self.master.after(1000, self.go_update)

    def increase_plot_size(self):
        self.plot_distance += 2
        self.plot_ora_item_size += 2
        self.plot_devider -= 1
        self.graph_spread_y += 1
        self.red_spacer += 1

    def decrease_plot_size(self):
        self.plot_distance -= 2
        self.plot_ora_item_size -= 2
        self.plot_devider += 1
        self.graph_spread_y -= 1
        self.red_spacer -= 1

    def create_infographic(self):
        # create lines to show information about the tweets
        self.canvas.create_line(
            self.initial_x,
            self.current_zero_line,
            self.initial_x + 1920,
            self.current_zero_line,
            fill="blue", dash=(4, 4))

        self.canvas.create_line(
            self.initial_x,
            self.current_zero_line - 10 * self.plot_distance,
            self.initial_x + 1920,
            self.current_zero_line - 10 * self.plot_distance,
            fill="red", dash=(4, 4))

        self.canvas.create_line(
            self.initial_x,
            self.current_zero_line + 10 * self.plot_distance,
            self.initial_x + 1920,
            self.current_zero_line + 10 * self.plot_distance,
            fill="green", dash=(4, 4))

        # show information on the end of the lines
        self.canvas.create_text(
            1250,
            self.current_zero_line - 11 * self.plot_distance,
            text="-10")

        self.canvas.create_text(
            1250,
            self.current_zero_line + 11 * self.plot_distance,
            text="+10")

    def auto_update(self):
        if self.started:
            self.auto_updating = not self.auto_updating
            self.go_update()

    def go_update(self):
        self.canvas.delete("all")
        self.update_plot(self.canvas, self.master)

    def go_right(self):
        self.initial_x -= 50
        self.go_update()

    def go_left(self):
        self.initial_x += 50
        self.go_update()
