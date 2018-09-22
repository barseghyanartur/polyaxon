import { connect } from 'react-redux';
import { Dispatch } from 'redux';

import { AppState } from '../constants/types';
import { MetricModel } from '../models/metric';

import * as experimentActions from '../actions/experiment';
import * as actions from '../actions/metrics';
import Metrics from '../components/metrics/metrics';
import { ChartViewModel } from '../models/chartView';

export function mapStateToProps(state: AppState, params: any) {
  const useLastFetchedViews = () => {
    const viewIds = state.chartViews.lastFetched.ids;
    const count = state.chartViews.lastFetched.count;
    const views: ChartViewModel[] = [];
    viewIds.forEach(
      (viewId: number, idx: number) => {
        views.push(state.chartViews.byIds[viewId]);
      });
    return {views, count};
  };
  const useLastFetchedParams = () => {
    const experimentNames = state.experimentsParams.lastFetched.names;
    let count = state.experimentsParams.lastFetched.count;
    const experimentParams: { [id: number]: { [key: string]: any } } = {};
    experimentNames.forEach(
      (experimentName: string, idx: number) => {
        const declarations = state.experimentsParams.byUniqueNames[experimentName].declarations;
        const id = state.experimentsParams.byUniqueNames[experimentName].id;
        experimentParams[id] = declarations;
      });
    if (!count && params.experiment) {
      experimentParams[params.experiment.id] = params.experiment.declarations
      count = 1;
    }
    return {experimentParams, count};
  };

  const useLastFetchedMetrics = () => {
    const metricIds = state.metrics.lastFetched.ids;
    const count = state.metrics.lastFetched.count;
    const metrics: MetricModel[] = [];
    metricIds.forEach(
      (metricId: number, idx: number) => {
        metrics.push(state.metrics.byIds[metricId]);
      });
    return {metrics, count};
  };

  const results = useLastFetchedMetrics();
  const viewsResults = useLastFetchedViews();
  const experimentParamsResults = useLastFetchedParams();

  return {
    metrics: results.metrics,
    views: viewsResults.views,
    resource: params.resource,
    params: experimentParamsResults.experimentParams,
    count: results.count,
  };
}

export interface DispatchProps {
  fetchData?: () => actions.MetricsAction;
  fetchParamsData?: () => experimentActions.ExperimentAction;
  fetchViews?: () => actions.MetricsAction;
  createView?: (data: ChartViewModel) => actions.MetricsAction;
  deleteView?: (viewId: number) => actions.MetricsAction;
}

export function mapDispatchToProps(dispatch: Dispatch<actions.MetricsAction>, params: any): DispatchProps {
  return {
    fetchData: () => {
      return dispatch(actions.fetchMetrics(params.project, params.resource, params.id));
    },
    fetchParamsData: () => {
      if (params.resource === 'groups') {
        const filters = {
          group: params.id,
          declarations: true
        };
        return dispatch(experimentActions.fetchExperiments(params.project, filters));
      }
    },
    fetchViews: () => {
      return dispatch(actions.fetchChartViews(params.project, params.resource, params.id));
    },
    createView: (data: ChartViewModel) => {
      return dispatch(actions.createChartView(params.project, params.resource, params.id, data));
    },
    deleteView: (viewId: number) => {
      return dispatch(actions.deleteChartView(params.project, params.resource, params.id, viewId));
    },
  };
}

export default connect(mapStateToProps, mapDispatchToProps)(Metrics);
