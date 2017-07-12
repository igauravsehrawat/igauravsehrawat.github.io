FROM ruby:2.2.7

EXPOSE 4000

WORKDIR /blog

ADD . /blog

RUN gem install bundler

RUN bundle install

CMD ["jekyll", "serve", "--watch"]
