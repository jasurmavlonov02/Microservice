import Translator from './i18n'

class Analytics {
  constructor(gapi, token, viewId, domIds) {
    this.gapi = gapi
    this.token = token
    this.domIds = domIds
    this.viewId = viewId
    this.t = new Translator($('html').attr('lang'))
  }

  init(timedelta) {
    const self = this
    this.gapi.analytics.ready(function () {
      self.run(timedelta)
    })
  }

  run(timedelta) {
    const self = this
    const gapi = this.gapi

    const spinner = $('<div />')
      .css({
        textAlign: 'center',
        padding: '3rem 0',
        color: '#aaa',
      })
      .append($('<i />', { class: 'fa fa-spinner fa-spin fa-3x fa-fw' }))

    for (const prop in this.domIds) {
      if (['traffic', 'popular', 'browsers', 'acquisition', 'audience', 'social'].indexOf(prop) !== -1) {
        $('#' + this.domIds[prop]).append(spinner.clone())
      }
    }

    const errorCb = (containerId) => () => {
      $('#' + containerId).empty()

      const message = $('<div />')
        .css({
          textAlign: 'center',
          padding: '3rem 0',
          color: '#aaa',
        })
        .text(this.t.get('retrieveDataError'))

      $('#' + containerId).append(message)
    }

    gapi.analytics.ready(function () {
      /**
       * Authorize the user with an access token obtained server side.
       */
      gapi.analytics.auth.authorize({
        serverAuth: {
          access_token: self.token,
        },
      })
      /**
       * Create a new ViewSelector2 instance to be rendered inside of an
       * element with the id "view-selector-container".
       */
      const viewSelector = new gapi.analytics.ViewSelector({
        container: self.domIds.viewSelector,
      })
      viewSelector.execute()

      const baseQuery = {
        ids: 'ga:' + self.viewId,
        'start-date': timedelta,
        'end-date': 'yesterday',
      }

      /**
       * Creates a new DataChart instance showing sessions over the past 15 days.
       */
      const dataChart1 = new gapi.analytics.googleCharts.DataChart({
        query: {
          ...baseQuery,
          metrics: 'ga:sessions,ga:users',
          dimensions: 'ga:date',
        },
        chart: {
          container: self.domIds.traffic,
          type: 'LINE',
          options: {
            width: '100%',
          },
        },
      })
      const trafficTimeout = setTimeout(errorCb(self.domIds.traffic), 20000)
      dataChart1.on('error', errorCb(self.domIds.traffic))
      dataChart1.on('success', () => clearTimeout(trafficTimeout))
      dataChart1.execute()
      /**
       * Creates a new DataChart instance showing top 5 most popular pages
       */
      const dataChart2 = new gapi.analytics.googleCharts.DataChart({
        query: {
          ...baseQuery,
          metrics: 'ga:pageviews',
          dimensions: 'ga:pagePath',
          sort: '-ga:pageviews',
          'max-results': 7,
        },
        chart: {
          container: self.domIds.popular,
          type: 'PIE',
          options: {
            width: '100%',
            pieHole: 4 / 9,
          },
        },
      })
      const popularTimeout = setTimeout(errorCb(self.domIds.popular), 20000)
      dataChart2.on('error', errorCb(self.domIds.popular))
      dataChart2.on('success', () => clearTimeout(popularTimeout))
      dataChart2.execute()
      /**
       * Creates a new DataChart instance showing top borwsers
       */
      const dataChart3 = new gapi.analytics.googleCharts.DataChart({
        query: {
          ...baseQuery,
          metrics: 'ga:sessions',
          dimensions: 'ga:browser',
          sort: '-ga:sessions',
          'max-results': 7,
        },
        chart: {
          container: self.domIds.browsers,
          type: 'PIE',
          options: {
            width: '100%',
            pieHole: 4 / 9,
          },
        },
      })
      const browsersTimeout = setTimeout(errorCb(self.domIds.browsers), 20000)
      dataChart3.on('error', errorCb(self.domIds.browsers))
      dataChart3.on('success', () => clearTimeout(browsersTimeout))
      dataChart3.execute()
      /**
       * Creates a new DataChart instance showing top referral
       */
      const dataChart4 = new gapi.analytics.googleCharts.DataChart({
        query: {
          ...baseQuery,
          metrics: 'ga:sessions',
          dimensions: 'ga:source',
          sort: '-ga:sessions',
          'max-results': 7,
        },
        chart: {
          container: self.domIds.acquisition,
          type: 'PIE',
          options: {
            width: '100%',
            pieHole: 4 / 9,
          },
        },
      })
      const acquisitionTimeout = setTimeout(errorCb(self.domIds.acquisition), 20000)
      dataChart4.on('error', errorCb(self.domIds.acquisition))
      dataChart4.on('success', () => clearTimeout(acquisitionTimeout))
      dataChart4.execute()
      /**
       * Creates a new DataChart instance showing top visitors continents
       */
      const dataChart5 = new gapi.analytics.googleCharts.DataChart({
        query: {
          ...baseQuery,
          metrics: 'ga:sessions',
          dimensions: 'ga:country',
          sort: '-ga:sessions',
          'max-results': 7,
        },
        chart: {
          container: self.domIds.audience,
          type: 'PIE',
          options: {
            width: '100%',
            pieHole: 4 / 9,
          },
        },
      })
      const audienceTimeout = setTimeout(errorCb(self.domIds.audience), 20000)
      dataChart5.on('error', errorCb(self.domIds.audience))
      dataChart5.on('success', () => clearTimeout(audienceTimeout))
      dataChart5.execute()
      /**
       * Creates a new DataChart instance showing social interactions over the past 15 days.
       */
      const dataChart6 = new gapi.analytics.googleCharts.DataChart({
        query: {
          ...baseQuery,
          metrics: 'ga:socialInteractions',
          dimensions: 'ga:socialInteractionNetwork',
          sort: '-ga:socialInteractions',
          'max-results': 7,
        },
        chart: {
          container: self.domIds.social,
          type: 'PIE',
          options: {
            width: '100%',
            pieHole: 4 / 9,
          },
        },
      })
      const socialTimeout = setTimeout(errorCb(self.domIds.social), 20000)
      dataChart6.on('error', errorCb(self.domIds.social))
      dataChart6.on('success', () => clearTimeout(socialTimeout))
      dataChart6.execute()
    })
  }
}

export default Analytics
